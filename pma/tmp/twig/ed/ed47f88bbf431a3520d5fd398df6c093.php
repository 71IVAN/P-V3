<?php

use Twig\Environment;
use Twig\Error\LoaderError;
use Twig\Error\RuntimeError;
use Twig\Extension\SandboxExtension;
use Twig\Markup;
use Twig\Sandbox\SecurityError;
use Twig\Sandbox\SecurityNotAllowedTagError;
use Twig\Sandbox\SecurityNotAllowedFilterError;
use Twig\Sandbox\SecurityNotAllowedFunctionError;
use Twig\Source;
use Twig\Template;

/* server/user_groups/tab_list.twig */
class __TwigTemplate_c69c4d9d6c72c42e2ddd383795fff531 extends Template
{
    private $source;
    private $macros = [];

    public function __construct(Environment $env)
    {
        parent::__construct($env);

        $this->source = $this->getSourceContext();

        $this->parent = false;

        $this->blocks = [
        ];
    }

    protected function doDisplay(array $context, array $blocks = [])
    {
        $macros = $this->macros;
        // line 1
        echo "<fieldset class=\"pma-fieldset\">
    <legend>
        ";
        // line 3
        echo twig_escape_filter($this->env, ($context["title"] ?? null), "html", null, true);
        echo "
    </legend>
    ";
        // line 5
        $context['_parent'] = $context;
        $context['_seq'] = twig_ensure_traversable(($context["tab_details"] ?? null));
        foreach ($context['_seq'] as $context["_key"] => $context["tab_detail"]) {
            // line 6
            echo "        <div class=\"item\">
            <input type=\"checkbox\" class=\"checkall\"";
            // line 7
            echo twig_get_attribute($this->env, $this->source, $context["tab_detail"], "in_array", [], "any", false, false, false, 7);
            echo " name=\"";
            echo twig_escape_filter($this->env, ($context["level"] ?? null), "html", null, true);
            echo "_";
            echo twig_escape_filter($this->env, twig_get_attribute($this->env, $this->source, $context["tab_detail"], "tab", [], "any", false, false, false, 7), "html", null, true);
            echo "\" value=\"Y\">
            <label for=\"";
            // line 8
            echo twig_escape_filter($this->env, ($context["level"] ?? null), "html", null, true);
            echo "_";
            echo twig_escape_filter($this->env, twig_get_attribute($this->env, $this->source, $context["tab_detail"], "tab", [], "any", false, false, false, 8), "html", null, true);
            echo "\">
                <code>";
            // line 9
            echo twig_escape_filter($this->env, twig_get_attribute($this->env, $this->source, $context["tab_detail"], "tab_name", [], "any", false, false, false, 9), "html", null, true);
            echo "</code>
            </label>
        </div>
    ";
        }
        $_parent = $context['_parent'];
        unset($context['_seq'], $context['_iterated'], $context['_key'], $context['tab_detail'], $context['_parent'], $context['loop']);
        $context = array_intersect_key($context, $_parent) + $_parent;
        // line 13
        echo "</fieldset>
";
    }

    public function getTemplateName()
    {
        return "server/user_groups/tab_list.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  77 => 13,  67 => 9,  61 => 8,  53 => 7,  50 => 6,  46 => 5,  41 => 3,  37 => 1,);
    }

    public function getSourceContext()
    {
        return new Source("", "server/user_groups/tab_list.twig", "/home/vagrant/proyectos/pma/templates/server/user_groups/tab_list.twig");
    }
}
